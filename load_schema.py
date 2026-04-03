import pymysql

# Conectar como flask (novo usuário)
conn = pymysql.connect(host='localhost', user='flask', password='flask123', database='pi3')
cursor = conn.cursor()

try:
    # Ler e executar init.sql
    with open('init.sql', 'r', encoding='utf-8') as f:
        sql_content = f.read()
        # Dividir por ; e executar cada statement
        statements = sql_content.split(';')
        for statement in statements:
            statement = statement.strip()
            if statement:  # Pula statements vazios
                cursor.execute(statement)
                print(f"✓ Executado: {statement[:60]}...")
    
    conn.commit()
    print("\n✓ Tabelas e schema carregados com sucesso!\n")
    
except Exception as e:
    print(f"✗ Erro ao carregar schema: {e}")
    import traceback
    traceback.print_exc()
finally:
    cursor.close()
    conn.close()
