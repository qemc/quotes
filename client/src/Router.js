import { Routes, Route } from "react-router-dom";
import React from "react";
import HomePage from "./HomePage";
import Login from "./Login";
import Register from "./Register"





const Router = () => {
    return ( 
        <Routes>
            <Route path="/" element={<HomePage/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/register" element={<Register/>} />
        </Routes>
     );
}
 
export default Router;