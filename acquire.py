import os

def new_titanic_data():
    url = env.get_db_url('titanic_db')
    
    return pd.read_sql('SELECT * FROM passengers', url)

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile('titanic_dataframe.csv'):
        return pd.read_csv('titanic_dataframe.csv', index_col=0)
    
    else:
        url = env.get_db_url('titanic_db')
        df_titanic = pd.read_sql('SELECT * FROM passengers', url)
        df_titanic.to_csv('titanic_dataframe.csv')
        return df_titanic

def new_iris_data(): 
    url = env.get_db_url('iris_db')

    return pd.read_sql('''
    SELECT * FROM measurements
    JOIN species ON measurements.species_id = species.species_id
    ''', url)

def get_iris_data(): 
    filename = "iris.csv"

    if os.path.isfile('iris_data.csv'):
        return pd.read_csv('iris_data.csv', index_col=0)
    
    else: 
        url = env.get_db_url('iris_db')
        df_iris = pd.read_sql('''
        SELECT * FROM measurements
        JOIN species ON measurements.species_id = species.species_id
        ''', url)
        df_iris.to_csv('iris_data.csv')
        return df_iris
    
def new_telco_data(): 
    url = env.get_db_url('telco_churn')
    
    return pd.read_sql('''
    SELECT * FROM customers
    JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
    JOIN customer_payments ON customers.customer_id = customer_payments.customer_id
    JOIN customer_contracts ON customers.customer_id = customer_contracts.customer_id
    ''', url)

def get_telco_data(): 
    filename = "telco_churn.csv"

    if os.path.isfile('telco_data.csv'):
        return pd.read_csv('telco_data.csv', index_col=0)
    
    else: 
        url = env.get_db_url('telco_churn')
        df_telco = pd.read_sql('''
        SELECT * FROM customers
        JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
        JOIN customer_payments ON customers.customer_id = customer_payments.customer_id
        JOIN customer_contracts ON customers.customer_id = customer_contracts.customer_id
        ''', url)
        df_telco.to_csv('telco_data.csv')
        return df_telco