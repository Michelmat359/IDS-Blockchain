import React, { useState } from 'react';
import { retrieveData } from '../api';
import { TextField, Button, Typography, Box, Alert } from '@mui/material';

const RetrieveData = () => {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setResponse(null);
        setError(null);
        try {
            const result = await retrieveData({ "data.name": query });
            setResponse(result);
        } catch (err) {
            setError(err);
        }
    };

    return (
        <Box sx={{ padding: 2 }}>
            <Typography variant="h4" gutterBottom>Consultar Datos</Typography>
            <form onSubmit={handleSubmit}>
                <TextField
                    fullWidth
                    margin="normal"
                    label="Nombre"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    required
                />
                <Button variant="contained" color="primary" type="submit" sx={{ mt: 2 }}>
                    Consultar
                </Button>
            </form>
            {response && <Alert severity="info" sx={{ mt: 2 }}>{JSON.stringify(response)}</Alert>}
            {error && <Alert severity="error" sx={{ mt: 2 }}>{JSON.stringify(error)}</Alert>}
        </Box>
    );
};

export default RetrieveData;
