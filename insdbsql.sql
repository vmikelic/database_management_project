-- Active: 1663717527080@@127.0.0.1@3306
use cs482502;

#inserts data into database of cs482502

insert into Video(videoCode, videoLength) values (129,1024), (130,12460), (131,34000);

insert into Model(modelNo, width, height, weight, depth, screenSize) values 
('tvsam12345', 26.0, 20.0, 14.3, 1.3, 32.0),
('hdsam22345', 54.0, 30.0, 14.3, 1.2, 60.0),
('lesam32345', 68.0, 36.0, 14.3, 2.0, 72.0);

insert into Site(siteCode, type, address, phone) values
(1, 'restaurant', '800 E. University Ave, Las Cruces, NM 88001', '575-123-1234' ),
(2, 'bar', '8003 W. 5th, Las Vegas, NV 88901', '702-123-1234' ),
(3, 'restaurant', '512 Main St, Los Angeles, CA 90001', '213-777-1234' );

insert into DigitalDisplay(serialNo, schedulerSystem, modelNo) values
('452s33x121', 'Virtue', 'tvsam12345'),
('284s33hd21', 'Random', 'hdsam22345'),
('459s33le34', 'Smart', 'lesam32345');

insert into Client(clientId, name, phone, address) values
(20012, 'Doe, John', '232-77-0000', '12 S. First St., Atlanta, GA 34523'),
(20013, 'Aaron, Henry', '123-77-0453', '789 W Monroe Ave., Louisville, KY 38562'),
(20014, 'Little, Stewart', '444-72-0060', '34222 College Blvd, Los Angeles, CA 90001');

insert into TechnicalSupport(empId, name, gender) values
(10014, 'Brown, Charlie', 'M'),
(10015, 'Mouse, Mickey', 'M'),
(10016, 'Bunny, Bugs', 'M');

insert into Administrator(empId, name, gender) values
(10004, 'Simpson, Bart', 'M'),
(10005, 'Dinkley, Velma', 'F'),
(10006, 'VanPelt, Linus', 'M');

insert into Salesman(empId, name, gender) values
(00001, 'Peter', 'M'),
(00002, 'Mary', 'F'),
(00003, 'John', 'M'),
(00004, 'Mary', 'F');

insert into AirtimePackage(packageId, class, startDate, lastDate, frequency, videoCode) values
(913, 'economy', '2022-01-02', '2022-01-07', 2, 129),
(914, 'whole day', '2022-02-03', '2022-02-04', 1, 130),
(915, 'golden hours', '2022-04-03', '2022-04-03', 3, 131),
(916, 'economy', '2022-01-02', '2022-01-07', 2, 129),
(917, 'whole day', '2022-02-03', '2022-02-04', 1, 130),
(918, 'golden hours', '2022-04-03', '2022-04-03', 3, 131),
(919, 'economy', '2022-01-02', '2022-01-07', 2, 129),
(920, 'whole day', '2022-02-03', '2022-02-04', 1, 130),
(921, 'golden hours', '2022-04-03', '2022-04-03', 3, 131);

insert into AdmWorkHours(empId, day, hours) values
(10005, '2022-01-02', 8.50),
(10004, '2022-01-03', 8.00),
(10006, '2022-01-04', 9.00);

insert into Broadcasts(videoCode, siteCode) values
(129, 1),
(130, 2),
(131, 3);

insert into Administers(empId, siteCode) values
(10005, 2),
(10004, 1),
(10006, 3);

insert into Specializes(empId, modelNo) values
(10014, 'lesam32345'),
(10014, 'hdsam22345'),
(10015, 'tvsam12345');

insert into Purchases(clientId, empId, packageId, commissionRate) values
(20013, 00001, 913, 0.05),
(20013, 00001, 914, 0.08),
(20012, 00002, 915, 0.06),
(20012, 00002, 916, 0.04),
(20012, 00002, 917, 0.03),
(20014, 00003, 918, 0.05),
(20014, 00003, 919, 0.10);

insert into Locates(serialNo, siteCode) values
('284s33hd21', 1),
('459s33le34', 2),
('452s33x121', 3);
