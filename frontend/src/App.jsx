import MarkForm from "./FormCreating";
import './App.css';
import FileLoading from "./FileLoading";
import GetFile from "./GetFile"; // Стили
function App() {
    return (
        <div className="App">
            <h1>Марки Техники</h1>
            <MarkForm/>
            <FileLoading/>
            <GetFile/>
        </div>
    );
}

export default App;