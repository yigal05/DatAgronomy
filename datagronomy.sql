-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 03-05-2025 a las 01:50:30
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `datagronomy`
--
CREATE DATABASE IF NOT EXISTS `datagronomy` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `datagronomy`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cerdas`
--

DROP TABLE IF EXISTS `cerdas`;
CREATE TABLE IF NOT EXISTS `cerdas` (
  `Id_cerda` int NOT NULL AUTO_INCREMENT,
  `cod_cerda` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `raza` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `estado` enum('vacia','inseminada','gestante','lactancia') CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL DEFAULT 'vacia',
  PRIMARY KEY (`Id_cerda`),
  UNIQUE KEY `cod_cerda` (`cod_cerda`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `cerdas`
--

INSERT INTO `cerdas` (`Id_cerda`, `cod_cerda`, `fecha_nacimiento`, `raza`, `estado`) VALUES
(1, 'C001', '2023-01-15', 'Landrace', 'vacia'),
(2, 'C002', '2023-02-20', 'Yorkshire', 'inseminada'),
(3, 'C003', '2022-12-10', 'Duroc', 'gestante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `Id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `direccion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `telefono` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`Id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Id_cliente`, `nombre`, `direccion`, `telefono`) VALUES
(1, 'Agropecuaria La Finca', 'Calle 10 #5-20', '3101234567'),
(2, 'Distribuciones Pecuarias SAS', 'Carrera 25 #12-34', '3159876543'),
(3, 'Ganaderia El Rodeo', 'Finca La Esperanza', '3202468135');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lechones`
--

DROP TABLE IF EXISTS `lechones`;
CREATE TABLE IF NOT EXISTS `lechones` (
  `Id_lechon` int NOT NULL AUTO_INCREMENT,
  `cod_lechon` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `fecha_nac` date DEFAULT NULL,
  `raza` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `Id_lote` int DEFAULT NULL,
  `Id_madre` int DEFAULT NULL,
  PRIMARY KEY (`Id_lechon`),
  UNIQUE KEY `cod_lechon` (`cod_lechon`),
  KEY `Id_lote` (`Id_lote`),
  KEY `Id_madre` (`Id_madre`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `lechones`
--

INSERT INTO `lechones` (`Id_lechon`, `cod_lechon`, `fecha_nac`, `raza`, `Id_lote`, `Id_madre`) VALUES
(1, 'L001', '2024-03-01', 'Landrace', 1, 1),
(2, 'L002', '2024-03-01', 'Landrace', 1, 1),
(3, 'L003', '2024-03-10', 'Yorkshire', 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lotes`
--

DROP TABLE IF EXISTS `lotes`;
CREATE TABLE IF NOT EXISTS `lotes` (
  `Id_lote` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci,
  PRIMARY KEY (`Id_lote`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `lotes`
--

INSERT INTO `lotes` (`Id_lote`, `nombre`, `descripcion`) VALUES
(1, 'Lote 1', 'Corral principal de reproduccion'),
(2, 'Lote 2', 'Corral de levante'),
(3, 'Lote 3', 'Corral de gestacion'),
(4, 'Bodega', 'Bodega de insumos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `montas`
--

DROP TABLE IF EXISTS `montas`;
CREATE TABLE IF NOT EXISTS `montas` (
  `Id_monta` int NOT NULL AUTO_INCREMENT,
  `fecha_monta` date NOT NULL,
  `Id_cerda` int DEFAULT NULL,
  `Id_semen` int DEFAULT NULL,
  `fecha_parto` date DEFAULT NULL,
  `Id_usuario` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`Id_monta`),
  KEY `Id_cerda` (`Id_cerda`),
  KEY `Id_semen` (`Id_semen`),
  KEY `Id_usuario` (`Id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `montas`
--

INSERT INTO `montas` (`Id_monta`, `fecha_monta`, `Id_cerda`, `Id_semen`, `fecha_parto`, `Id_usuario`) VALUES
(1, '2024-02-01', 1, 1, '2024-05-25', 'user001'),
(2, '2024-02-10', 2, 2, '2024-06-03', 'user002');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mov_alimento`
--

DROP TABLE IF EXISTS `mov_alimento`;
CREATE TABLE IF NOT EXISTS `mov_alimento` (
  `Id_movimiento` int NOT NULL AUTO_INCREMENT,
  `tipo_alimento` enum('preiniciador','iniciacion','levante','engorde','finalizador','gestacion','lactancia') CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `cantidad_bultos` int DEFAULT NULL,
  `tipo_movimiento` enum('Entrada','Salida') CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `fecha_movimiento` date DEFAULT NULL,
  `id_lote` int DEFAULT NULL,
  PRIMARY KEY (`Id_movimiento`),
  KEY `id_lote` (`id_lote`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partos`
--

DROP TABLE IF EXISTS `partos`;
CREATE TABLE IF NOT EXISTS `partos` (
  `Id_parto` int NOT NULL AUTO_INCREMENT,
  `fecha_parto` date NOT NULL,
  `Id_cerda` int DEFAULT NULL,
  `Id_lote` int DEFAULT NULL,
  `cant_lechones` int DEFAULT NULL,
  `nacidos_muertos` int DEFAULT NULL,
  `cant_machos` int DEFAULT NULL,
  `cant_hembras` int DEFAULT NULL,
  `Id_usuario` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`Id_parto`),
  KEY `Id_cerda` (`Id_cerda`),
  KEY `Id_lote` (`Id_lote`),
  KEY `Id_usuario` (`Id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `partos`
--

INSERT INTO `partos` (`Id_parto`, `fecha_parto`, `Id_cerda`, `Id_lote`, `cant_lechones`, `nacidos_muertos`, `cant_machos`, `cant_hembras`, `Id_usuario`) VALUES
(1, '2024-05-25', 1, 1, 10, 1, 5, 4, 'user001'),
(2, '2024-06-03', 2, 2, 8, 0, 3, 5, 'user002');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `semen`
--

DROP TABLE IF EXISTS `semen`;
CREATE TABLE IF NOT EXISTS `semen` (
  `Id_semen` int NOT NULL AUTO_INCREMENT,
  `cod_semen` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `fecha_adquisicion` date DEFAULT NULL,
  `granja_adquisicion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `contacto_granja` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `raza` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`Id_semen`),
  UNIQUE KEY `cod_semen` (`cod_semen`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `semen`
--

INSERT INTO `semen` (`Id_semen`, `cod_semen`, `fecha_adquisicion`, `granja_adquisicion`, `contacto_granja`, `raza`) VALUES
(1, 'S001', '2024-01-20', 'Genetica Porcina SAS', '3115552211', 'Duroc'),
(2, 'S002', '2024-02-01', 'Semen Selecto LTDA', '3128889900', 'Pietrain');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `Id_usuario` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `nombre` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `apellido` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `usuario` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `contrasena` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `rol` enum('granjero','administrador') CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`Id_usuario`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id_usuario`, `nombre`, `apellido`, `usuario`, `contrasena`, `rol`) VALUES
('user001', 'Santiago', 'Arango', 'santiago', 'd48b165d1e5a63b56c7601e4269642e6a71fa90b2178a0212a1da5f7ee54255f', 'administrador'),
('user002', 'Valentina', 'Gomez', 'valentina', '6086d0c00085495558ee2dc7ba5a136de0a0c28ed46e4a957f0ec741e8d98966', 'granjero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE IF NOT EXISTS `ventas` (
  `Id_venta` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `cant_cerdos` int DEFAULT NULL,
  `cant_kilos` decimal(10,2) DEFAULT NULL,
  `precio_kilo` decimal(10,2) DEFAULT NULL,
  `Id_cliente` int DEFAULT NULL,
  PRIMARY KEY (`Id_venta`),
  KEY `Id_cliente` (`Id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`Id_venta`, `fecha`, `cant_cerdos`, `cant_kilos`, `precio_kilo`, `Id_cliente`) VALUES
(1, '2024-02-15', 5, 500.00, 2500.00, 1),
(2, '2024-03-01', 10, 1000.00, 2750.00, 2),
(3, '2025-04-28', 24, 163.00, 2000.00, 3),
(4, '2025-04-28', 50, 2000.00, 5300.00, 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
