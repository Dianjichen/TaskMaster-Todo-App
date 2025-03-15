import React, { useState } from "react";
import axios from "axios";

function TodoForm({ refreshTasks }) {
    const [title, setTitle] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/api/tasks/", { title, completed: false })
            .then(() => {
                setTitle("");
                refreshTasks();
            })
            .catch(error => console.error("Error adding task:", error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="New task..."
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <button type="submit">Add</button>
        </form>
    );
}

export default TodoForm;
