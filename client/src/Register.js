import React, { useState } from "react";
import httpClient from "./httpClient";


const Register = () => {

    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const RegisterUser = async () => {
        try {
            const response = await httpClient.post("http://127.0.0.1:5000/register",{
                email,
                username,
                password,
            });
            
            window.location.href = "/";
            
        } catch (error) {
            if(error.response.status === 401){
                alert("invalid credentials");
            }
        }
    }



    return ( 
        <div>
            
            <form>
                <div>
                    <label>Username: </label>
                    <input 
                        type="text"
                        value = {username}
                        id=""
                        onChange={(e)=>setUsername(e.target.value)}
                    />
                </div>
                <div>
                    <label>Email: </label>
                    <input 
                        type="text"
                        value = {email}
                        id=""
                        onChange={(e)=>setEmail(e.target.value)}
                    />
                </div>
                
                <div>
                    <label>password: </label>
                    <input 
                        type="text"
                        value = {password}
                        id=""
                        onChange={(e)=>setPassword(e.target.value)}
                    />
                </div>
                <div>
                    <button type="subbmit" onClick={RegisterUser}>
                        subbmit
                    </button>
                </div>

            </form>

        </div>
     );
}
 
export default Register;