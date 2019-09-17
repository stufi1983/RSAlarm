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
-- Struktur dari tabel `bedevents`
--

CREATE TABLE `bedevents` (
  `id` int(11) NOT NULL,
  `trigger_time` datetime DEFAULT NULL,
  `bed_id` int(11) NOT NULL,
  `status` varchar(5) DEFAULT NULL,
  `stop_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bedevents`
--
ALTER TABLE `bedevents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_bed_id` (`bed_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bedevents`
--
ALTER TABLE `bedevents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `bedevents`
--
ALTER TABLE `bedevents`
  ADD CONSTRAINT `fk_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `bedmap` (`bed`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
