import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoItem from "./TodoItem";

function TodoList() {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/tasks/")
            .then(response => setTodos(response.data))
            .catch(error => console.error("Error fetching tasks:", error));
    }, []);

    return (
        <div>
            <h2>To-Do List</h2>
            {todos.map(todo => (
                <TodoItem key={todo.id} todo={todo} />
            ))}
        </div>
    );
}

export default TodoList;
