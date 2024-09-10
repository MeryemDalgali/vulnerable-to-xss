# XSS Vulnerability Testing

This README provides an overview of XSS (Cross-Site Scripting) vulnerabilities found in the web application. XSS vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. The application contains several sections where different types of XSS vulnerabilities have been identified:

- **DOM-based XSS**
- **Stored XSS**
- **Reflected XSS**

## Vulnerability Testing Resources

For a comprehensive understanding of XSS vulnerabilities and testing methodologies, refer to the following OWASP Web Security Testing Guide resources:

- [Testing for Stored Cross-Site Scripting (XSS)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting)
- [Testing for Reflected Cross-Site Scripting (XSS)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [Testing for DOM-based Cross-Site Scripting (XSS)](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting)

## Vulnerability Examples

### 1. DOM-based XSS

The application allows manipulation of the URL hash to trigger a DOM-based XSS vulnerability. By appending a payload after the `#` symbol in the URL, you can execute arbitrary JavaScript in the context of the page.

![DOM-based XSS Example](https://github.com/user-attachments/assets/932e7d0e-962e-4104-9cf5-e3f401ac8472)
![DOM-based XSS Payload](https://github.com/user-attachments/assets/cf870ee1-d182-4e7a-b8d5-e60f94ef63be)
![DOM-based XSS Trigger](https://github.com/user-attachments/assets/94d2a5db-8364-49e3-b7f6-092689a0408d)

### 2. Stored XSS

The application allows users to comment on posts. A stored XSS vulnerability is present where an attacker can inject a malicious payload into a comment. This payload gets stored and executed whenever other users view the comment.

![Stored XSS Comment](https://github.com/user-attachments/assets/328e5b96-9b56-48ae-95b4-3ed9f3d07f18)
![Stored XSS Payload](https://github.com/user-attachments/assets/2c393bc6-cd29-4deb-a28e-8bb150fe18a1)

### 3. Reflected XSS

The application’s search functionality reflects user input directly back to the user. By injecting a payload into the search query, an attacker can trigger a reflected XSS vulnerability.

![Reflected XSS Search](https://github.com/user-attachments/assets/c6aff1d6-d8a2-4c07-bd63-25b0fe3a2094)
![Reflected XSS Payload](https://github.com/user-attachments/assets/6a4bfdd4-089a-478b-8c41-1ed9d68bc20b)

## Conclusion

Understanding these vulnerabilities helps in securing web applications against XSS attacks. Regular testing and validation of user inputs are crucial to prevent such vulnerabilities. For more details on preventing XSS, refer to the OWASP guidelines linked above.
