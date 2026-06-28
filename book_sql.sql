-- mysql statements for book_sql database

-- create 1st table
create database book_sql;

create table myapp_book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    summary TEXT,
    category VARCHAR(100),
    reward_points INT DEFAULT 0,
    cover_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 查詢
SELECT * FROM book_sql.myapp_book;

-- insert data into 1st table
INSERT INTO book_sql.myapp_book
(title, author, summary, category, reward_points, cover_url, created_at)
VALUES
('原子習慣', 'James Clear', '介紹如何透過微小習慣累積長期成長，適合用於學習養成。', '自我成長', 20, 'https://picsum.photos/300/400?1', NOW()),
('深度學習力', 'Cal Newport', '說明如何提升專注力，減少干擾，培養高品質學習能力。', '學習方法', 25, 'https://picsum.photos/300/400?2', NOW()),
('刻意練習', 'Anders Ericsson', '探討專家養成的方法，強調回饋、目標與持續修正。', '技能養成', 30, 'https://picsum.photos/300/400?3', NOW()),
('被討厭的勇氣', '岸見一郎、古賀史健', '以阿德勒心理學探討自我肯定、人際關係與目標建立。', '心理成長', 15, 'https://picsum.photos/300/400?4', NOW()),
('學會如何學習', 'Barbara Oakley', '介紹有效學習技巧，包含記憶、理解、複習與時間管理。', '學習方法', 20, 'https://picsum.photos/300/400?5', NOW());


-- create 2nd table
create table myapp_readingrecord (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    reader_name VARCHAR(255) NOT NULL,
    note longtext NOT NULL,
    progress INT DEFAULT 0,
    is_completed BOOLEAN DEFAULT FALSE,
    earned_points INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES myapp_book(id)
);

-- query
SELECT * FROM book_sql.myapp_readingrecord;

-- truncate table myapp_readingrecord;

-- insert data into 2nd table
INSERT INTO book_sql.myapp_readingrecord
(book_id, reader_name, note, progress, is_completed, earned_points, created_at)
VALUES
(1, 'Sandy', '原子習慣讓我了解微小改變的重要性。', 100, TRUE, 20, NOW()),
(2, 'Amy', '專注力的培養需要持續練習。', 80, FALSE, 0, NOW()),
(3, 'John', '刻意練習是一種有目標的學習方式。', 100, TRUE, 30, NOW()),
(4, 'Mary', '心理學的觀點很值得反思。', 70, FALSE, 0, NOW()),
(5, 'David', '這本書提供許多實用技巧。', 100, TRUE, 20, NOW()),

(1, 'Kevin', '每天進步一點點很重要。', 90, FALSE, 0, NOW()),
(2, 'Eric', '深度工作能提升效率。', 100, TRUE, 25, NOW()),
(3, 'Helen', '透過反覆練習提升能力。', 60, FALSE, 0, NOW()),
(4, 'Cindy', '學會接受自己的不足。', 100, TRUE, 15, NOW()),
(5, 'Tom', '學習方法值得實踐。', 100, TRUE, 20, NOW()),

(1, 'Lisa', '養成好習慣需要時間。', 100, TRUE, 20, NOW()),
(2, 'Jack', '排除干擾很重要。', 50, FALSE, 0, NOW()),
(3, 'Peter', '專家都是透過刻意練習而來。', 100, TRUE, 30, NOW()),
(4, 'Rose', '改變思維方式很有幫助。', 100, TRUE, 15, NOW()),
(5, 'Anna', '有效學習可以節省很多時間。', 100, TRUE, 20, NOW()),

(1, 'Lucas', '值得推薦給學生閱讀。', 100, TRUE, 20, NOW()),
(2, 'Wendy', '提高專注力的方法很多。', 75, FALSE, 0, NOW()),
(3, 'Leo', '持續練習比天賦更重要。', 100, TRUE, 30, NOW()),
(4, 'Nancy', '人際關係的觀念很受用。', 100, TRUE, 15, NOW()),
(5, 'Chris', '內容淺顯易懂。', 85, FALSE, 10, NOW()),

(1, 'Tony', '建立習慣循環很有趣。', 100, TRUE, 20, NOW()),
(2, 'Sophia', '專注力是一種能力。', 100, TRUE, 25, NOW()),
(3, 'Ivy', '目標設定非常重要。', 70, FALSE, 0, NOW()),
(4, 'Jason', '阿德勒心理學值得深入研究。', 100, TRUE, 15, NOW()),
(5, 'Grace', '適合作為入門學習書籍。', 100, TRUE, 20, NOW()),

(1, 'Ben', '習慣影響人生。', 100, TRUE, 20, NOW()),
(2, 'Emma', '專注力訓練需要環境配合。', 90, FALSE, 0, NOW()),
(3, 'Kevin', '練習品質比數量更重要。', 100, TRUE, 30, NOW()),
(4, 'Olivia', '閱讀後很有收穫。', 100, TRUE, 15, NOW()),
(5, 'Daniel', '學習技巧可以立即運用。', 100, TRUE, 20, NOW()),

(1, 'Maggie', '從小習慣開始改變。', 100, TRUE, 20, NOW()),
(2, 'Sandy', '深度工作理論很有啟發。', 100, TRUE, 25, NOW()),
(3, 'Vivian', '需要持續回饋與修正。', 100, TRUE, 30, NOW()),
(4, 'Frank', '心理成長值得長期實踐。', 100, TRUE, 15, NOW()),
(5, 'Cathy', '對學生很有幫助。', 80, FALSE, 10, NOW()),

(1, 'Sandy', '簡單但實用的觀念。', 100, TRUE, 20, NOW()),
(2, 'Sandy', '改善分心問題。', 100, TRUE, 25, NOW()),
(3, 'George', '建立訓練機制很重要。', 90, FALSE, 0, NOW()),
(4, 'Scott', '重新認識自己。', 100, TRUE, 15, NOW()),
(5, 'Mark', '非常推薦閱讀。', 100, TRUE, 20, NOW()),

(1, 'Sunny', '每天都能應用。', 100, TRUE, 20, NOW()),
(2, 'Scott', '適合上班族閱讀。', 100, TRUE, 25, NOW()),
(3, 'Jenny', '透過練習提升能力。', 100, TRUE, 30, NOW());


-- deep query

SELECT
    r.id,
    r.reader_name,
    b.title AS book_name,
    r.progress,
    r.is_completed,
    r.earned_points
FROM book_sql.myapp_readingrecord r
INNER JOIN book_sql.myapp_book b
    ON r.book_id = b.id;



-- git
-- git remote add origin https://github.com/sandy789456-cyber/ReadingManagement.git
-- git branch -f main HEAD 
-- git push origin main



