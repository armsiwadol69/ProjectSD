-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2021 at 08:35 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tempandhumi_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `rec_used`
--

CREATE TABLE `rec_used` (
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `temp` int(11) NOT NULL,
  `humi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rec_used`
--

INSERT INTO `rec_used` (`date`, `temp`, `humi`) VALUES
('2021-02-12 15:05:04', 19, 20),
('2021-02-12 15:05:17', 20, 30),
('2021-02-12 15:15:15', 22, 35),
('2021-02-12 16:40:59', 35, 20),
('2021-02-12 16:41:20', 29, 55),
('2021-02-12 16:55:33', 26, 69),
('2021-02-12 17:29:11', 19, 90),
('2021-02-12 18:18:42', 23, 44),
('2021-02-12 18:21:44', 25, 10),
('2021-02-12 19:13:15', 27, 15),
('2021-02-12 19:13:27', 26, 33),
('2021-02-13 05:49:38', 31, 15),
('2021-02-13 14:12:23', 20, 30),
('2021-02-13 17:17:53', 23, 0),
('2021-02-15 07:18:44', 39, 30),
('2021-02-19 17:17:14', 31, 54),
('2021-02-19 17:22:12', 31, 54),
('2021-02-19 17:22:52', 31, 54),
('2021-02-19 17:24:31', 31, 54),
('2021-02-19 17:25:58', 31, 54),
('2021-02-19 17:28:23', 31, 54),
('2021-02-19 17:28:32', 31, 54),
('2021-02-19 17:30:23', 31, 54),
('2021-02-19 17:30:28', 31, 54),
('2021-02-19 17:30:34', 31, 54),
('2021-02-19 17:30:39', 31, 54),
('2021-02-19 17:30:45', 31, 54),
('2021-02-19 17:30:51', 31, 54),
('2021-02-19 17:39:47', 34, 44),
('2021-02-19 17:39:52', 34, 44),
('2021-02-19 17:39:58', 35, 44),
('2021-02-19 17:40:03', 34, 44),
('2021-02-19 17:40:09', 34, 44),
('2021-02-19 17:40:14', 34, 44),
('2021-02-19 17:40:20', 34, 44),
('2021-02-19 17:40:25', 34, 44),
('2021-02-19 17:40:31', 34, 44),
('2021-02-19 17:40:36', 34, 44),
('2021-02-19 18:15:48', 30, 54),
('2021-02-19 18:15:56', 30, 54),
('2021-02-19 18:16:05', 30, 54),
('2021-02-19 18:43:24', 30, 55),
('2021-02-19 19:31:51', 30, 53),
('2021-02-19 19:33:44', 30, 53);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rec_used`
--
ALTER TABLE `rec_used`
  ADD PRIMARY KEY (`date`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
