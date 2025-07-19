<?php
// Load file user
$users = file('users.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

function cekQuery($query, $users) {
    // Simulasi SQL Injection: parsing query abal-abal
    foreach ($users as $row) {
        list($username, $password) = explode(':', $row);

        // Ganti variabel $user di dalam "query" dengan username dari txt
        $parsedQuery = str_replace("'", "", $query);
        $parsedQuery = str_replace("user", "'$username'", $parsedQuery);

        // Eval "query" abal-abal, kalau true anggap ketemu
        if (@eval("return $parsedQuery;")) {
            return true;
        }
    }
    return false;
}

$feedback = "";
if (isset($_GET['username'])) {
    $input = $_GET['username'];

    // Simulasi blind SQLi: input dijadikan "query"
    // Misalnya: ' == 'admin' akan jadi true
    $query = "'$input' == user";  // jadi: 'admin' == 'admin'

    if (cekQuery($query, $users)) {
        $feedback = "User ditemukan!";
    } else {
        $feedback = "User tidak ditemukan!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Blind SQLi File-Based</title>
</head>
<body>
    <h2>Simulasi Login (Vulnerable)</h2>
    <form method="get">
        <input type="text" name="username" placeholder="Cek username">
        <input type="submit" value="Submit">
    </form>

    <p><?= htmlspecialchars($feedback) ?></p>
</body>
</html>
