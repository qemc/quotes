import React from "react";
import httpClient from "./httpClient";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

const HomePage = () => {

    
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [id, setId] = useState("");


    useEffect(()=>{
       ( async ()=>{

            try {
                const response = await httpClient.get("http://127.0.0.1:5000/@me", {
                    email,
                    username,
                    id,
                })
            } catch (error) {
                console.log("Not authenticated");
            }
    
        })();
    
    },[])

  




    return (
        <div>
            <h1>home page</h1>
            

        </div>
    );
}
 
export default HomePage;