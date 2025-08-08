<?php
include 'conexion.php';
$usuarios = $pdo->query("SELECT * FROM usuarios")->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>CRUD de Usuarios</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="container mt-5">
    <h1 class="mb-4">Lista de Usuarios</h1>
    <a href="crear.php" class="btn btn-success mb-3">Agregar Usuario</a>
    <table class="table table-bordered table-striped">
        <thead class="table-dark">
            <tr>
                <th>ID</th><th>Nombre</th><th>Correo</th><th>Edad</th><th>Acciones</th>
            </tr>
        </thead>
        <tbody>
        <?php foreach ($usuarios as $usuario): ?>
        <tr>
            <td><?= $usuario['id'] ?></td>
            <td><?= $usuario['nombre'] ?></td>
            <td><?= $usuario['correo'] ?></td>
            <td><?= $usuario['edad'] ?></td>
            <td>
                <a href="editar.php?id=<?= $usuario['id'] ?>" class="btn btn-primary btn-sm">Editar</a>
                <a href="eliminar.php?id=<?= $usuario['id'] ?>" class="btn btn-danger btn-sm" onclick="return confirm('¿Eliminar este usuario?')">Eliminar</a>
            </td>
        </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
