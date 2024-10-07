import MarkForm from "./FormCreating";
import './App.css';
import FileLoading from "./FileLoading"; // Стили
function App() {
    return (
        <div className="App">
            <h1>Марки Техники</h1>
            <MarkForm/>
            <FileLoading/>
        </div>
    );
}

export default App;