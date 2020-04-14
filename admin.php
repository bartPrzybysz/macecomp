<!DOCTYPE htlm>
<html>

<head>
    <title>Admin</title>
    <style>
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
        }
    </style>

</html>

</head>

<body>
    <h1>Admin Page</h1>
    <img src="img/under_construction.webp" class="center">
    <p>
        <?php if($_POST['roles'] == 'urn:lti:role:ims/lis/Instructor'): ?>
        Administrative page appears here, since user is an instructor.
        <?php else: ?>
        Access denied, user is not an instructor
        <?php endif; ?>
    <p>
    GET:
    <pre>
        <?= print_r($_GET); ?>
    </pre>
    POST:
    <pre>
        <?= print_r($_POST); ?>
    </pre>
</body>

<footer>
    Using php <?= phpversion(); ?>
</footer>

</html>