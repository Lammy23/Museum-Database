DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM; 
USE MUSEUM;

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT
( Id_no                 CHAR(5)         NOT NULL,
  Title                 VARCHAR(100)    NOT NULL,
  Year_of_creation      INT                     ,
  Country_of_origin     VARCHAR(20)             ,
  Epoch                 VARCHAR(20)             ,
  Object_description    VARCHAR(200)    NOT NULL,
  Ownership_Type        VARCHAR(20)     NOT NULL,
  Date_acquired         DATE                    ,
  Object_status         VARCHAR(20)             ,
  Cost                  INT                     ,
  Date_borrowed         DATE                    ,
  Date_returned         DATE                    ,
  
  PRIMARY KEY (Id_no) 
  );


DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
    Id_no       CHAR(5)     NOT NULL,
    Material    VARCHAR(50) NOT NULL,
    Height      INT         NOT NULL,
    Style       VARCHAR(50) NOT NULL,

    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS STATUE;
CREATE TABLE STATUE (
    Id_no       CHAR(5)     NOT NULL,
    Material    VARCHAR(50) NOT NULL,
    Height      INT NOT NULL,
    Style       VARCHAR(50) NOT NULL,

    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
    Id_no       CHAR(5)     NOT NULL,
    Style       VARCHAR(50) NOT NULL,
    Object_type VARCHAR(20) NOT NULL,
    
	PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING
( Id_no CHAR(5) NOT NULL,
  Paint_type VARCHAR(20) NOT NULL,
  Drawn_on VARCHAR(20) NOT NULL,
  Style VARCHAR(20) NOT NULL,
  
  PRIMARY KEY (Id_no),
  FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
  Id_no                 CHAR(5)         NOT NULL,
  Artist_name 			VARCHAR(50)     NOT NULL,
  Artist_description    VARCHAR(100)    		,
  Birth_date            DATE            		,
  Death_date            DATE                    ,
  Artist_Epoch          VARCHAR(20)     		,
  Main_style            VARCHAR(20)     		,
  Artist_Country_of_origin VARCHAR(20)     		,
  
  PRIMARY KEY (Id_no, Artist_name),
  FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS (
  Id_no             CHAR(5)       NOT NULL,
  Exhibition_name   VARCHAR(100)   NOT NULL,
  Start_date        DATE          NOT NULL,
  End_date          DATE          NOT NULL,
  
  PRIMARY KEY (Id_no, Exhibition_name),
  FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
  Id_no                   CHAR(5)       NOT NULL,
  Collection_name         VARCHAR(100)   NOT NULL,
  Collection_description  VARCHAR(100)  NOT NULL,
  Collection_type         VARCHAR(20)   NOT NULL,
  Contact_Fname           VARCHAR(20)   NOT NULL,
  Contact_Lname           VARCHAR(20)   NOT NULL,
  Contact_Phone           VARCHAR(20)   NOT NULL,
  
  PRIMARY KEY (Id_no, Collection_name),
  FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON DELETE CASCADE
);

INSERT INTO ART_OBJECT VALUES
-- PAINTINGS
('PA001', 'Herman von Wedigh III (died 1560)', 1532, 'Germany', 'Renaissance', 'A Portrait of a young man resting his arm on a table.', 'Permanent', '2022-10-10', 'On display', 250000, NULL, NULL),
('PA002', 'Portrait of a man in royal livery', 1535, 'England', 'Renaissance', 'A Portrait of an artisan or attendant in the royal household', 'Permanent', '2022-10-10', 'On display', 70000, NULL, NULL),
('PA003', 'Trompe lOeil Still Life', 1678, 'Netherlands', 'Golden Age', 'A random assortment of everyday items, with illusionary elements', 'Permanent', '2022-10-20', 'In storage', 208000, NULL, NULL),
('PA004', 'Violin and Grapes', 1912, 'Spain', 'Modern', 'Perspective shifting cubism representation of violin and grapes.', 'Permanent', '2022-10-20', 'In storage', 2940000, NULL, NULL),
('PA005', 'Imitation', 1887, 'USA', 'Modern', 'Realistic painting of an American bill and mail stamps, using the illusionary elements of trompe-loeil.', 'Permanent', '2022-10-20', 'In storage', 5100, NULL, NULL),
('PA006', 'The Raft of the Medusa', 1819, 'France', 'Victorian', 'This large painting represents a tragic episode in the history of the french colonial navy.', 'Borrowed', NULL, NULL, 12000000, '2022-01-10', '2023-11-09'),
('PA007', 'Mona Lisa', 1517, 'Italy', 'High Renaissance', 'The infamous portrait of Lisa del Gioncondo', 'Borrowed', NULL, NULL, 400000000, '2022-01-10', '2023-11-09'),
('PA008', 'The Oath of the Horatii', 1785, 'Italy', 'Victorian', 'It represents a major subject in the legendary history of Ancient Rome , where the Horatii brothers defended the city of Rome in single combat against the Curiatii champions of the city of Alba.', 'Borrowed', NULL, NULL, 510000, '2022-01-10', '2023-11-09'),

-- SCULPTURES
('SC001', 'Portrait Bust of John Fisher, Bishop of Rochester', 1515, 'England', 'Renaissance', 'A painted sculpture representing John Fischer of Rochester.', 'Permanent', '2022-10-10', 'In storage', 15000, NULL, NULL),
('SC002', 'The Absinthe Glass', 1914, 'France', 'Modern', 'A abstract representation of an absinthe glass using wax cast in bronze.', 'Permanent', '2022-10-20', 'In storage', 389000, NULL, NULL),
('SC003', 'Cone of Entemena', -2400, 'Ancient Mesopotamia', 'Ancient', 'Describes the generations-long struggle over land and the Tigris and Euphrates canal through the etches all around the cone. Created by the court historian of King Entemena', 'Borrowed', NULL, NULL, 2567000, '2022-01-10', '2023-11-09'),

-- STATUES
('ST001', 'Armor Garniture of George Clifford (1558 to 1605), Third Earl of Cumberland', 1586, 'England', 'Renaissance', 'Armor made of steel, gold, leather, and textiles', 'Permanent', '2022-10-10', 'On display', 160000, NULL, NULL),
('ST002', 'Power figure', 1850, 'Congo', 'Victorian', 'A staue of a Vili man of the Congo made of wood, iron, blades, nails, fragments, and fiber cord.', 'Permanent', '2022-09-09', 'On loan', NULL, NULL, NULL),
('ST003', 'Aphrodite of Melos', -50, 'Greece', 'Hellenistic', 'An infamous greek statue standing 6 foot 7 inches depicting the greek god of love, Aphrodite', 'Borrowed', NULL, NULL, 67250000, '2022-01-10', '2023-11-09'),

-- OTHERS
('OT001', 'Martyrdom of the Seven Maccabee Brothers and Their Mother', 1535, 'Netherlands', 'Renaissance', 'Represents The Old Testament story of King Antiochus IV Epiphanes', 'Permanent', '2022-10-10', 'On display', 780000, NULL, NULL),
('OT002', 'Wine Cup on a High Foot (Tazza)', 1600, 'England', 'Renaissance', 'A wide shallow wine cup made of gilded silver harboring a small dove in the middle', 'Permanent', '2022-10-10', 'On display', 67000, NULL, NULL),
('OT003', 'Guitar and Wine Glass', 1912, 'Spain', 'Modern', 'Cubism representation of a guitar and a wine glass using a collage of media.', 'Permanent', '2022-10-20', 'In storage', 92000, NULL, NULL),
('OT004', '108 (Face Jug Series)', 2019, 'USA', 'Modern', 'Inspired by the pottery made by the black potters of Old Edgefield, SC.', 'Permanent', '2022-09-09', 'On loan', NULL, NULL, NULL),
('OT005', 'Applying Pressure', 2021, 'USA', 'Modern', 'Abstract ceramic jug placed on a red oak table.', 'Permanent', '2022-09-09', 'On loan', NULL, NULL, NULL),
('OT006', 'Ceasarea Cup', 350, 'Palestine', 'Ancient', 'A bronze bowl with gold and silver details depicting the founding of Ceasarea of Palestine', 'Borrowed', NULL, NULL, 95000, '2022-01-10', '2023-11-09');

INSERT INTO PAINTING VALUES
('PA001', 'Oil', 'Oak', 'Portrait painting'),
('PA002', 'Oil', 'Parchment', 'Portrait painting'),
('PA003', 'Oil', 'Canvas', 'trompe-loeil'),
('PA004', 'Oil', 'Canvas', 'Cubism'),
('PA005', 'Oil', 'Canvas', 'trompe-loeil'),
('PA006', 'Oil', 'Canvas', 'Romantic'),
('PA007', 'Oil', 'Poplar panel', 'Portrait painting'),
('PA008', 'Oil', 'Canvas', 'Neoclassicism');
    
INSERT INTO SCULPTURE VALUES
('SC001', 'Polychrome terracotta', 61.6, 'Portrait bust'),
('SC002', 'Wax cast in bronze', 22.5, 'Cubism'),
('SC003', 'Stone', 27, 'Ancient Mesopotamian sculpture');

INSERT INTO STATUE VALUES
('ST001', 'Metal', 176.5, 'Armor garniture'),
('ST002', 'Wood, metal, cord', 103.5, 'Wood statue'),
('ST003', 'Marble', 201, 'Ancient Greek sculpture');

INSERT INTO OTHER VALUES
('OT001', 'Stained glass', 'Glass pane'),
('OT002', 'Metalwork-silver', 'Wine cup'),
('OT003', 'Cubism', 'Paperboard'),
('OT004', 'Salt-fired porcelain', 'Jug'),
('OT005', 'Painted ceramic', 'Jug on table'),
('OT006', 'Metalwork-bronze', 'Cup');

INSERT INTO ARTIST VALUES
('PA001', 'Hans Holbein the Younger', 'German artist known for his portraits.', '1498-01-01', '1543-01-01', 'Renaissance', 'Portrait painting', 'Germany'),
('PA002', 'Hans Holbein the Younger', 'German artist known for his portraits.', '1498-01-01', '1543-01-01', 'Renaissance', 'Portrait painting', 'Germany'),
('PA003', 'Samuel van Hoogstraten', 'Dutch painter and art theory author.', '1627-08-02', '1678-10-19', 'Golden Age', 'Painting', 'Netherlands'),
('PA004', 'Pablo Picasso', 'Revolutionary painter, known for pioneering the style of cubism.', '1881-10-25', '1973-04-08', 'Modern', 'Cubism', 'Spain'),
('PA005', 'John Haberle', 'American trompe-loeil painter, replicated paper bills so exactly he raised suspicions of forgery', '1861-01-25', '1933-04-01', 'Modern', 'trompe-loeil', 'USA'),
('PA006', 'Théodore Géricault', 'One of the greatest French romantic artists', '1791-09-26', '1824-01-26', 'Victorian', 'Romantic', 'France'),
('PA007', 'Leonardo da Vinci', 'Revolutionary painter, draughtsman, engineer, scientist, theorist, sculptor, and architect.', '1452-12-19', '1519-11-08', 'High Renaissance', 'Portrait painting', 'Italy'),
('PA008', 'Jacques-Louis David', 'French painter and conventionalist, considered the pioneer of the neoclassical movement.', '1748-10-25', '1824-04-08', 'Victorian', 'Neoclassicism', 'France'),
('SC001', 'Pietro Torrigiano', 'Italian sculpter, known for breaking Michealangelos nose.', '1472-01-01', '1528-01-01', 'Renaissance', 'Sculpture', 'Italy'),
('SC002', 'Pablo Picasso', 'Revolutionary painter, known for pioneering the style of cubism.', '1881-10-25', '1973-04-08', 'Modern', 'Cubism', 'Spain'),
('ST001', 'Jacob Halder', 'The master armorer, head of the royal workshops of Grenwich.', '1558-01-01', '1608-01-01', 'Renaissance', 'Armor', 'England'),
('OT001', 'Dirk Vellert', 'Artist known for stained glass creations', '1480-01-01', '1547-01-01', 'Renaissance', 'Stained glass', 'Netherlands'),
('OT003', 'Pablo Picasso', 'Revolutionary painter, known for pioneering the style of cubism.', '1881-10-25', '1973-04-08', 'Modern', 'Cubism', 'Spain'),
('OT004', 'Simone Leigh', 'Chicago born artist known for her sculpting and social work', '1967-01-01', NULL, 'Modern', 'African Art', 'USA'),
('OT005', 'Woody De Othelo', 'American ceramist and painter', '1991-01-01', NULL, 'Modern', 'Ceramist', 'USA');

INSERT INTO EXHIBITIONS VALUES
('PA001', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('PA002', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('PA003', 'Cubism and the Trompe lOeil Tradition', '2020-01-01', '2021-01-01'),
('SC001', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('SC002', 'Cubism and the Trompe lOeil Tradition', '2020-01-01', '2021-01-01'),
('ST001', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('PA004', 'Cubism and the Trompe lOeil Tradition', '2020-01-01', '2021-01-01'),
('PA005', 'Cubism and the Trompe lOeil Tradition', '2020-01-01', '2021-01-01'),
('OT001', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('OT002', 'The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('OT003', 'Cubism and the Trompe lOeil Tradition', '2020-01-01', '2021-01-01'),
('OT004', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05'),
('ST002', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05'),
('OT005', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05');

INSERT INTO COLLECTIONS VALUES
('PA006', 'Masterpieces of the Louvre', 'Timeless masterpieces provided by the Louvre museum', 'Art', 'Jonas', 'Huber', '403-403-4033'),
('PA007', 'Masterpieces of the Louvre', 'Timeless masterpieces provided by the Louvre museum', 'Art', 'Jonas', 'Huber', '403-403-4033'),
('ST003', 'Masterpieces of the Louvre', 'Timeless masterpieces provided by the Louvre museum', 'Art', 'Jonas', 'Huber', '403-403-4033'),
('SC003', 'Major Events in History', 'A collection of some of the most influential moments in history, captured in time', 'Art', 'Olamikun', 'Aluko', '403-304-3044'),
('OT006', 'Major Events in History', 'A collection of some of the most influential moments in history, captured in time', 'Art', 'Olamikun', 'Aluko', '403-304-3044'),
('PA008', 'Major Events in History', 'A collection of some of the most influential moments in history, captured in time', 'Art', 'Olamikun', 'Aluko', '403-304-3044');