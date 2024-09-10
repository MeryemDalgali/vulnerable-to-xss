Before trying the lab, you can use this resource to look at how and why all these vulnerabilities exist.
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting

The interface of the application is as shown below. 

![Ekran görüntüsü 2024-09-10 150650](https://github.com/user-attachments/assets/932e7d0e-962e-4104-9cf5-e3f401ac8472)

As a convenience for the first attempt, I have provided a hint in the application interface “Use the hash in the URL to manipulate this message” 

When we come to the end of the URL and type the following command after #, we will have DOM based XSS. 

![Ekran görüntüsü 2024-09-10 150846](https://github.com/user-attachments/assets/cf870ee1-d182-4e7a-b8d5-e60f94ef63be)
![Ekran görüntüsü 2024-09-10 150816](https://github.com/user-attachments/assets/94d2a5db-8364-49e3-b7f6-092689a0408d)


There is a section in the application that allows us to comment on the last post, and when we come here, when we enter the following payload, it leads to a stored xss vulnerability. 
![Ekran görüntüsü 2024-09-10 130522](https://github.com/user-attachments/assets/328e5b96-9b56-48ae-95b4-3ed9f3d07f18)
![Ekran görüntüsü 2024-09-10 131134](https://github.com/user-attachments/assets/2c393bc6-cd29-4deb-a28e-8bb150fe18a1)

And finally, a search section appears. It reflects each value it receives from the user to the user. We have manipulated this place with a paylaod that will lead to reflected xss vulnerability. 
![Ekran görüntüsü 2024-09-10 131237](https://github.com/user-attachments/assets/c6aff1d6-d8a2-4c07-bd63-25b0fe3a2094)
![Ekran görüntüsü 2024-09-10 131214](https://github.com/user-attachments/assets/6a4bfdd4-089a-478b-8c41-1ed9d68bc20b)

