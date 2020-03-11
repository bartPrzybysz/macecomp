<!DOCTYPE htlm>
<html>

<head>
    <title>Index</title>
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
    <h1>Index of macecomp subdomain :)</h1>
    <img src="img/under_construction.webp" class="center">
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