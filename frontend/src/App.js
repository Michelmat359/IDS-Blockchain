import React from 'react';
import StoreData from './components/StoreData';
import RetrieveData from './components/RetrieveData';
import { AppBar, Toolbar, Typography, Box } from '@mui/material';

function App() {
    return (
        <Box>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" sx={{ flexGrow: 1 }}>
                        Gestión de Datos con Blockchain e IDS
                    </Typography>
                </Toolbar>
            </AppBar>
            <Box sx={{ padding: 3 }}>
                <StoreData />
                <RetrieveData />
            </Box>
        </Box>
    );
}

export default App;
