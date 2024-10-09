import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Forum() {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const fetchMessages = async () => {
            const response = await axios.get('http://localhost:5000/api/messages');
            setMessages(response.data);
        };
        fetchMessages();
    }, []);

    return (
        <div className="mt-4">
            {messages.map((msg) => (
                <div key={msg.id} className="alert alert-primary">
                    <strong>{msg.username}:</strong>
                    <p>{msg.content}</p>
                </div>
            ))}
        </div>
    );
}

export default Forum;
