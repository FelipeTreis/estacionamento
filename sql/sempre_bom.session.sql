CREATE TABLE estacionamento(
    id INTEGER PRIMARY NOT NULL DEFAULT nextval('estacionamento_id_seq'::regclass)
    veiculo VARCHAR(9) NOT NULL,
    tempo INT NOT NULL,
    valor NUMERIC CHECK(valor > 0)NOT NULL
);