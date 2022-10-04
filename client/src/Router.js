import { Routes, Route } from "react-router-dom";
import React from "react";
import HomePage from "./HomePage";
import Login from "./Login";

const Router = () => {
    return ( 
        <Routes>
            <Route path="/" element={<HomePage/>} />
            <Route path="/login" element={<Login/>} />
        </Routes>
     );
}
 
export default Router;