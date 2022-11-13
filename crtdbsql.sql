-- Active: 1663717527080@@127.0.0.1@3306
CREATE DATABASE IF NOT EXISTS cs482502;
USE cs482502;
CREATE TABLE IF NOT EXISTS Video 
(
    videoCode INT,
    videoLength INT,
    PRIMARY KEY(videoCode)
);
CREATE TABLE IF NOT EXISTS Model 
(
    modelNo CHAR(10),
    width NUMERIC(6,2),
    height NUMERIC(6,2),
    weight NUMERIC(6,2),
    depth NUMERIC(6,2),
    screenSize NUMERIC(6,2),
    PRIMARY KEY(modelNo)
);
CREATE TABLE IF NOT EXISTS Site
(
    siteCode INT,
    type VARCHAR(16) CHECK (type = 'bar' OR type = 'restaurant'),
    address VARCHAR(100),
    phone VARCHAR(16),
    PRIMARY KEY(siteCode)
);
CREATE TABLE IF NOT EXISTS DigitalDisplay
(
    serialNo CHAR(10),
    schedulerSystem CHAR(10) CHECK (schedulerSystem = 'Random' OR schedulerSystem = 'Smart' OR schedulerSystem = 'Virtue'),
    modelNo CHAR(10),
    PRIMARY KEY(serialNo),
    FOREIGN KEY(modelNo) REFERENCES Model(modelNo) ON delete set null ON update cascade
);
CREATE TABLE IF NOT EXISTS Client
(
    clientId INT,
    name VARCHAR(40),
    phone VARCHAR(16),
    address VARCHAR(100),
    PRIMARY KEY(clientId)
);
CREATE TABLE IF NOT EXISTS TechnicalSupport
(
    empId INT,
    name VARCHAR(40),
    gender CHAR(1),
    PRIMARY KEY(empId)
);
CREATE TABLE IF NOT EXISTS Administrator
(
    empId INT,
    name VARCHAR(40),
    gender CHAR(1),
    PRIMARY KEY(empId)
);
CREATE TABLE IF NOT EXISTS Salesman
(
    empId INT,
    name VARCHAR(40),
    gender CHAR(1),
    PRIMARY KEY(empId)
);
CREATE TABLE IF NOT EXISTS AirtimePackage
(
    packageId INT,
    class VARCHAR(16) CHECK ( class = 'economy' OR class = 'whole day' OR class = 'golden hours'),
    startDate DATE,
    lastDate DATE,
    frequency INT,
    videoCode INT,
    PRIMARY KEY(packageId)
);
CREATE TABLE IF NOT EXISTS AdmWorkHours
(
    empId INT,
    day DATE,
    hours NUMERIC(4,2),
    PRIMARY KEY(empId,day),
    FOREIGN KEY(empId) REFERENCES Administrator(empId) ON delete cascade ON update cascade
);
CREATE TABLE IF NOT EXISTS Broadcasts
(
    videoCode INT,
    siteCode INT,
    PRIMARY KEY(videoCode,siteCode),
    FOREIGN KEY(videoCode) REFERENCES Video(videoCode) ON delete cascade ON update cascade,
    FOREIGN KEY(siteCode) REFERENCES Site(siteCode) ON delete cascade ON update cascade
);
CREATE TABLE IF NOT EXISTS Administers
(
    empId INT,
    siteCode INT,
    PRIMARY KEY(empId,siteCode),
    FOREIGN KEY(empId) REFERENCES Administrator(empId) ON delete cascade ON update cascade,
    FOREIGN KEY(siteCode) REFERENCES Site(siteCode) ON delete cascade ON update cascade
);
CREATE TABLE IF NOT EXISTS Specializes
(
    empId INT,
    modelNo CHAR(10),
    PRIMARY KEY(empId,modelNo),
    FOREIGN KEY(empId) REFERENCES TechnicalSupport(empId) ON delete cascade ON update cascade,
    FOREIGN KEY(modelNo) REFERENCES Model(modelNo) ON delete cascade ON update cascade
);
CREATE TABLE IF NOT EXISTS Purchases
(
    clientId INT,
    empId INT,
    packageId INT,
    commissionRate NUMERIC(4,2),
    PRIMARY KEY(clientId,empId,packageId),
    FOREIGN KEY(clientId) REFERENCES Client(clientId) ON delete cascade ON update cascade,
    FOREIGN KEY(empId) REFERENCES Salesman(empId) ON delete cascade ON update cascade,
    FOREIGN KEY(packageId) REFERENCES AirtimePackage(packageId) ON delete cascade ON update cascade
);
CREATE TABLE IF NOT EXISTS Locates
(
    serialNo CHAR(10),
    siteCode INT,
    PRIMARY KEY(serialNo,siteCode),
    FOREIGN KEY(serialNo) REFERENCES DigitalDisplay(serialNo) ON delete cascade ON update cascade,
    FOREIGN KEY(siteCode) REFERENCES Site(siteCode) ON delete cascade ON update cascade
);
