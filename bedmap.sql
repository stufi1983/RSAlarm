-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 17 Sep 2019 pada 14.39
-- Versi Server: 10.1.37-MariaDB-0+deb9u1
-- PHP Version: 7.0.33-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `antrianku`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `bedmap`
--

CREATE TABLE `bedmap` (
  `bed` int(5) NOT NULL,
  `room` int(5) NOT NULL,
  `bed_name` varchar(37) DEFAULT NULL,
  `room_name` varchar(37) DEFAULT NULL,
  `light_status` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bedmap`
--

INSERT INTO `bedmap` (`bed`, `room`, `bed_name`, `room_name`, `light_status`) VALUES
(1, 1, 'Bed 1', 'Ruang A', NULL),
(2, 1, 'Bed 21', 'Ruang A', NULL),
(3, 1, 'Bed 31', 'Ruang A', NULL),
(4, 1, 'Bed 41', 'Ruang A', NULL),
(5, 1, 'Bed 51', 'Ruang A', NULL),
(6, 1, 'Bed 61', 'Ruang A', NULL),
(7, 1, 'Kamar Mandi', 'Ruang A', NULL),
(8, 2, 'Bed 1', 'Ruang B', NULL),
(9, 2, 'Bed 21', 'Ruang B', NULL),
(10, 2, 'Bed 31', 'Ruang B', NULL),
(11, 2, 'Bed 41', 'Ruang B', NULL),
(12, 2, 'Bed 51', 'Ruang B', NULL),
(13, 2, 'Bed 61', 'Ruang B', NULL),
(14, 2, 'Kamar Mandi', 'Ruang B', NULL),
(15, 3, 'Bed 1', 'Ruang C', NULL),
(16, 3, 'Bed 21', 'Ruang C', NULL),
(17, 3, 'Bed 31', 'Ruang C', NULL),
(18, 3, 'Bed 41', 'Ruang C', NULL),
(19, 3, 'Bed 51', 'Ruang C', NULL),
(20, 3, 'Bed 61', 'Ruang C', NULL),
(21, 3, 'Kamar Mandi', 'Ruang C', NULL),
(22, 4, 'Bed 1', 'Ruang D', NULL),
(23, 4, 'Bed 21', 'Ruang D', NULL),
(24, 4, 'Bed 31', 'Ruang D', NULL),
(25, 4, 'Bed 41', 'Ruang D', NULL),
(26, 4, 'Bed 51', 'Ruang D', NULL),
(27, 4, 'Bed 61', 'Ruang D', NULL),
(28, 4, 'Kamar Mandi', 'Ruang D', NULL),
(29, 5, 'Bed', 'Ruang isolasi', NULL),
(30, 5, 'Kamar Mandi', 'Ruang isolasi', NULL),
(31, 6, 'Bed', 'Ruang Tindakan', NULL),
(32, 6, 'Kamar Mandi', 'Ruang Tindakan', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bedmap`
--
ALTER TABLE `bedmap`
  ADD PRIMARY KEY (`bed`),
  ADD UNIQUE KEY `bed` (`bed`),
  ADD KEY `bed_2` (`bed`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
