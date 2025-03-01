erDiagram
    USER {
        int id PK
        string username
        string passwordHash
        string email
        string role
        datetime createdAt
    }

    PROFILE {
        int id PK
        int userId FK "ссылка на USER.id"
        string firstName
        string lastName
        string avatarUrl
        text bio
        datetime createdAt
        datetime updatedAt
    }

    FRIENDSHIP {
        int id PK
        int userIdOne FK "ссылка на USER.id"
        int userIdTwo FK "ссылка на USER.id"
        string status
        datetime createdAt
        datetime updatedAt
    }
