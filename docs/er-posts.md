erDiagram
    POST {
        UUID id PK
        UUID authorId FK "ссылка на USER.id"
        string title
        string content
        datetime createdAt
        datetime updatedAt
    }
    
    COMMENT {
        UUID id PK
        UUID postId FK "ссылка на POST.id"
        UUID authorId FK "ссылка на USER.id"
        string text
        datetime createdAt
    }


    POST ||--|{ COMMENT : "может содержать"
