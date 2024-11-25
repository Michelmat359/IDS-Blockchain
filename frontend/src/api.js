import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000'; // Asegúrate de que sea la URL correcta

export const storeData = async (data) => {
    try {
        const response = await axios.post(`${API_URL}/store`, data, {
            headers: {
                "Content-Type": "application/json",
            },
        });
        return response.data;
    } catch (error) {
        console.error("Error al almacenar datos:", error);
        throw error.response?.data || { error: "Error desconocido" };
    }
};

export const retrieveData = async (query) => {
    try {
        const response = await axios.get(`${API_URL}/retrieve`, {
            params: query,
            headers: {
                "Content-Type": "application/json",
            },
        });
        return response.data;
    } catch (error) {
        console.error("Error al recuperar datos:", error);
        throw error.response?.data || { error: "Error desconocido" };
    }
};
