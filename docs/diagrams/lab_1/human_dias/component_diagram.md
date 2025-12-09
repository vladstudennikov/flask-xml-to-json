```mermaid
componentDiagram
    actor User

    node "User's Browser" as Browser {
        component [Web Interface]
    }

    node "Web Server" as Server {
        component [Flask Application] as Flask
        component [Conversion Logic] as Logic
    }

    User -->> Browser
    Browser -->> Flask : HTTP Requests
    Flask -->> Logic : Calls conversion functions
```
