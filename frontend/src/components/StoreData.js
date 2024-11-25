import React, { useState } from 'react';
import { storeData } from '../api';
import { TextField, Button, Typography, Box, Alert } from '@mui/material';

const StoreData = () => {
    const [formData, setFormData] = useState({ name: '', value: '', timestamp: '' });
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setResponse(null);
        setError(null);
        try {
            const result = await storeData(formData);
            setResponse(result);
        } catch (err) {
            setError(err);
        }
    };

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4" gutterBottom>Subir Datos</Typography>
            <form onSubmit={handleSubmit}>
                <TextField
                    fullWidth
                    margin="normal"
                    label="Nombre"
                    name="name"
                    onChange={handleChange}
                    required
                />
                <TextField
                    fullWidth
                    margin="normal"
                    label="Valor"
                    name="value"
                    type="number"
                    onChange={handleChange}
                    required
                />
                <TextField
                    fullWidth
                    margin="normal"
                    label="Timestamp"
                    name="timestamp"
                    type="datetime-local"
                    onChange={handleChange}
                    required
                />
                <Button variant="contained" color="primary" type="submit" sx={{ mt: 2 }}>
                    Guardar
                </Button>
            </form>
            {response && <Alert severity="success" sx={{ mt: 2 }}>Datos almacenados con éxito.</Alert>}
            {error && <Alert severity="error" sx={{ mt: 2 }}>{JSON.stringify(error)}</Alert>}
        </Box>
    );
};

export default StoreData;
