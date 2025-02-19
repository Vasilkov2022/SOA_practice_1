erDiagram
    STATISTICS {
        UUID id PK
        UUID postId FK "ссылка на POST.id"
        int likesCount
        int viewsCount
        int commentsCount
        datetime lastUpdated
    }

    LIKE_EVENT {
        UUID id PK
        UUID postId
        UUID userId
        datetime createdAt
    }

    VIEW_EVENT {
        UUID id PK
        UUID postId
        UUID userId
        datetime createdAt
    }

    COMMENT_EVENT {
        UUID id PK
        UUID postId
        UUID commentId
        UUID userId
        datetime createdAt
    }
