# PyPostgreSQL Client

Ejemplo de conexión de un cliente PostgreSQL en Ubuntu 18.04

## Instalación

Paquetes para Ubuntu

```bash
sudo apt-get install postgresql -y 
sudo apt-get install postgresql-contrib -y
```

Se crea la base de datos y el usuario

```bash
sudo -u postgres psql -c "CREATE USER test WITH PASSWORD 'test'"
sudo -u postgres psql -c "CREATE DATABASE test OWNER test ENCODING 'UTF8'"
```

Módulos python para la ejecución del script

```bash
sudo pip install psycopg2-binary
sudo pip install dataset
```

## Ejecución

```bash
sudo python src/index.py
```

## Referencias

[Documentación Dataset](https://dataset.readthedocs.io/)