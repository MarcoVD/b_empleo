cat > ~/PycharmProjects/bolsa_empleo/check_db_connection.py << 'EOF'
#!/usr/bin/env python
import sys
import os
import django
from django.db import connection

# Configurar el entorno Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bolsa_empleo.settings")  # Ajusta esto a tu nombre de proyecto
django.setup()

def check_connection():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            print("✅ Conexión exitosa a PostgreSQL")
            print(f"   Versión: {version}")
            return True
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")
        return False

if __name__ == "__main__":
    print("Verificando conexión a PostgreSQL desde Django...")
    check_connection()
EOF

# Hacer ejecutable
chmod +x ~/PycharmProjects/bolsa_empleo/check_db_connection.py
