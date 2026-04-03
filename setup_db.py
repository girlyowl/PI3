import pymysql

# Conectar como root
conn = pymysql.connect(host='localhost', user='root')
cursor = conn.cursor()

try:
    # Criar banco de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS pi3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print("✓ Banco 'pi3' criado/verificado")
    
    # Criar usuário flask
    cursor.execute("CREATE USER IF NOT EXISTS 'flask'@'localhost' IDENTIFIED BY 'flask123';")
    print("✓ Usuário 'flask' criado/verificado")
    
    # Dar permissões
    cursor.execute("GRANT ALL PRIVILEGES ON pi3.* TO 'flask'@'localhost';")
    print("✓ Permissões concedidas")
    
    # Flush privileges
    cursor.execute("FLUSH PRIVILEGES;")
    print("✓ Privileges atualizadas")
    
    conn.commit()
    print("\n✓ Banco de dados configurado com sucesso!\n")
    
except Exception as e:
    print(f"✗ Erro: {e}")
finally:
    cursor.close()
    conn.close()
