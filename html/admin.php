<?php
//https://stackoverflow.com/a/43397264
session_start();
if(!isset($_SESSION['login'])) {
    header('LOCATION:login.php'); die();
}
?>
<html>
<head>
    <title>Admin Page</title>
</head>
<body>
This is admin page view able only by logged in users.
</body>
</html>