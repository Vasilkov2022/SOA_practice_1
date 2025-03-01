erDiagram
    POST {
        int id PK
        UUID authorId FK "ссылка на USER.id"
        string title
        string content
        datetime createdAt
        datetime updatedAt
    }

    
    
    COMMENT {
        int id PK
        UUID postId FK "ссылка на POST.id"
        UUID authorId FK "ссылка на USER.id"
        string text
        datetime createdAt
    }


    POST ||--|{ COMMENT : "может содержать"

    ATTACHMENT {
        int id PK
        UUID postId FK "ссылка на POST.id"
        string fileName
        string contentType
        long fileSize
        datetime createdAt
        datetime updatedAt
    }

    POST ||--|{ ATTACHMENT : "может иметь вложения"
