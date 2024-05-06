import express from 'express';

const router = express.Router();

router.get('/f', (req, res) => {
    console.log("Test");
});