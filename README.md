<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS Vulnerability Testing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2 {
            color: #333;
        }
        .example-img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            margin: 10px 0;
        }
        .example-description {
            margin-bottom: 20px;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>XSS Vulnerability Testing</h1>

    <p>This README provides an overview of XSS (Cross-Site Scripting) vulnerabilities found in the web application. XSS vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. The application contains several sections where different types of XSS vulnerabilities have been identified:</p>
    <ul>
        <li><strong>DOM-based XSS</strong></li>
        <li><strong>Stored XSS</strong></li>
        <li><strong>Reflected XSS</strong></li>
    </ul>

    <h2>Vulnerability Testing Resources</h2>
    <p>For a comprehensive understanding of XSS vulnerabilities and testing methodologies, refer to the following OWASP Web Security Testing Guide resources:</p>
    <ul>
        <li><a href="https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting" target="_blank">Testing for Stored Cross-Site Scripting (XSS)</a></li>
        <li><a href="https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting" target="_blank">Testing for Reflected Cross-Site Scripting (XSS)</a></li>
        <li><a href="https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting" target="_blank">Testing for DOM-based Cross-Site Scripting (XSS)</a></li>
    </ul>

    <h2>Vulnerability Examples</h2>

    <h3>1. DOM-based XSS</h3>
    <p>The application allows manipulation of the URL hash to trigger a DOM-based XSS vulnerability. By appending a payload after the <code>#</code> symbol in the URL, you can execute arbitrary JavaScript in the context of the page.</p>
    <img src="https://github.com/user-attachments/assets/932e7d0e-962e-4104-9cf5-e3f401ac8472" alt="DOM-based XSS Example" class="example-img">
    <img src="https://github.com/user-attachments/assets/cf870ee1-d182-4e7a-b8d5-e60f94ef63be" alt="DOM-based XSS Payload" class="example-img">
    <img src="https://github.com/user-attachments/assets/94d2a5db-8364-49e3-b7f6-092689a0408d" alt="DOM-based XSS Trigger" class="example-img">

    <h3>2. Stored XSS</h3>
    <p>The application allows users to comment on posts. A stored XSS vulnerability is present where an attacker can inject a malicious payload into a comment. This payload gets stored and executed whenever other users view the comment.</p>
    <img src="https://github.com/user-attachments/assets/328e5b96-9b56-48ae-95b4-3ed9f3d07f18" alt="Stored XSS Comment" class="example-img">
    <img src="https://github.com/user-attachments/assets/2c393bc6-cd29-4deb-a28e-8bb150fe18a1" alt="Stored XSS Payload" class="example-img">

    <h3>3. Reflected XSS</h3>
    <p>The application’s search functionality reflects user input directly back to the user. By injecting a payload into the search query, an attacker can trigger a reflected XSS vulnerability.</p>
    <img src="https://github.com/user-attachments/assets/c6aff1d6-d8a2-4c07-bd63-25b0fe3a2094" alt="Reflected XSS Search" class="example-img">
    <img src="https://github.com/user-attachments/assets/6a4bfdd4-089a-478b-8c41-1ed9d68bc20b" alt="Reflected XSS Payload" class="example-img">

    <h2>Conclusion</h2>
    <p>Understanding these vulnerabilities helps in securing web applications against XSS attacks. Regular testing and validation of user inputs are crucial to prevent such vulnerabilities. For more details on preventing XSS, refer to the OWASP guidelines linked above.</p>
</body>
</html>

