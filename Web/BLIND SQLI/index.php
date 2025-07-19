<?php
$users = file('users.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$feedback = "";

if (isset($_GET['input'])) {
    $input = $_GET['input'];
    $found = false;

    foreach ($users as $line) {
        list($username, $password) = explode(':', trim($line));
        $query = str_replace("user", "'$username'", $input);
        $code = "return ($query);";

        try {
            if (eval($code)) {
                $found = true;
                break;
            }
        } catch (Throwable $e) {
            $found = false;
        }
    }

    $feedback = $found ? "User ditemukan!" : "User tidak ditemukan!";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Blind SQLi Simulasi (Fix)</title>
</head>
<body>
    <h2>Blind SQL Injection Simulasi (File-Based)</h2>
    <form method="get">
        <input type="text" name="input" placeholder="Masukkan ekspresi" style="width:300px;">
        <input type="submit" value="Submit">
    </form>

    <p><strong>Feedback:</strong> <?= htmlspecialchars($feedback) ?></p>
</body>
</html>
