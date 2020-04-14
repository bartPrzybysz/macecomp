<!DOCTYPE htlm>
<html>

<head>
    <title>Question</title>
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
    <h1>Question Page</h1>
    <img src="img/under_construction.webp" class="center">
    <p>
        This is where question <b><?= $_POST['resource_link_title']; ?></b>
        will appear for student <b><?= $_POST['lis_person_sourcedid']; ?></b>
    </p>
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