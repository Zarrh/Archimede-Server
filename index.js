import express from 'express';
import { PORT } from './config.js';
import path from 'path';

const __dirname = path.resolve(); // Root
const paths = ['/', '/files', '/mej', '/experiences', '/us', '/staff', '/login']; // Basic links

const app = express();

app.use(express.static(path.join(__dirname, './dist'))); // UI files
app.use(express.static(path.join(__dirname, '/articles'))); // Articles files
app.use(express.static(path.join(__dirname, '/mejs'))); // Mejs files
app.use(express.static(path.join(__dirname, '/experiences'))); // Experiences files
//app.use(express.static(path.join(__dirname, '/experiences/Ricerca Operativa_2013-2014'))); // Experiences files
//app.use(express.static(path.join(__dirname, '/experiences/Matrici_2014-2015'))); // Experiences files

paths.forEach(_path => {
    app.get(_path, (req, res) => {
        res.header('X-Content-Type-Options', 'text/html');
        res.header('X-Frame-Options', 'DENY');
        res.sendFile(path.join(__dirname, 'dist', 'index.html'));
    });
}); // UI GET requests routing

app.get('/articles:article', (req, res) => {
    res.sendFile(path.join(__dirname, 'articles', `${req.params.article.substring(1)}`));
}); // Articles GET requests routing

app.get('/articles/essays:essay', (req, res) => {
    res.sendFile(path.join(__dirname, 'articles/essays', `${req.params.essay.substring(1)}`));
}); // Essays GET requests routing

app.get('/mejs:mej', (req, res) => {
    res.sendFile(path.join(__dirname, 'mejs', `${req.params.mej.substring(1)}`));
}); // Mejs GET requests routing

app.get('/experiences:experience', (req, res) => {
    res.sendFile(path.join(__dirname, 'experiences', `${req.params.experience.substring(1)}`));
}); // Experiences GET requests routing

app.use((req, res, next) => {
    const error = new Error('Resource not found');
    error.status = 404;
    next(error);
}); // Error GET requests routing

app.use((err, req, res, next) => {
    res.status(err.status || 500);
    /*res.json({
      error: {
        message: err.message
      }
    });*/
}); // Error handling

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});