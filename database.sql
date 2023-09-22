-- SQLite
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    store_type VARCHAR(1) NOT NULL CHECK (store_type in ('A','B','C')),
    store_size INTEGER NOT NULL,
    UNIQUE (store_type,store_size)
);

CREATE TABLE features (
    features_id INTEGER PRIMARY KEY,
    store_id INTEGER NOT NULL,
    date DATE NOT NULL,
    temperature INTEGER NOT NULL,
    fuel_price REAL NOT NULL,
    markdown1 REAL NOT NULL,
    markdown2 REAL NOT NULL,
    markdown3 REAL NOT NULL,
    markdown4 REAL NOT NULL,
    markdown5 REAL NOT NULL,
    cpi REAL NOT NULL,
    unemployment REAL NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
);

CREATE TABLE depts (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR(255) NOT NULL
);

CREATE TABLE sales (
    sales_id INTEGER PRIMARY KEY,
    store_id INTEGER NOT NULL,
    dept_id INTEGER NOT NULL,
    date DATE NOT NULL,
    weekly_sales REAL NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores (store_id),
    FOREIGN KEY (dept_id) REFERENCES depts (dept_id)
);

CREATE TABLE managers (
    manager_id INTEGER PRIMARY KEY,
    store_id INTEGER NOT NULL,
    manager_name VARCHAR(255) NOT NULL,
    years_as_manager INTEGER NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
);
