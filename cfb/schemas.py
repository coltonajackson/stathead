SCHEMA_SCRIPT = """CREATE TABLE IF NOT EXISTS players (
    id TEXT PRIMARY KEY,
    name TEXT,
    position TEXT,
    team TEXT,
    first_year DATE,
    last_year DATE
);

CREATE TABLE IF NOT EXISTS offense (
    id TEXT PRIMARY KEY,
    name TEXT,
    position TEXT,
    team TEXT,
    first_year DATE,
    last_year DATE
);

CREATE TABLE IF NOT EXISTS defense (
    id TEXT PRIMARY KEY,
    name TEXT,
    position TEXT,
    team TEXT,
    first_year DATE,
    last_year DATE
);

CREATE TABLE IF NOT EXISTS special_teams (
    id TEXT PRIMARY KEY,
    name TEXT,
    position TEXT,
    team TEXT,
    first_year DATE,
    last_year DATE
);
"""