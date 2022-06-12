import React, { useEffect, useState, useContext } from "react";
import SideBar from "/components/SideBar/SideBar";
import styles from "/styles/ClassSearch.module.css";
import UserInfo from "/components/UserInfo/UserInfo";
import SearchResults from "/components/SearchResults/SearchResults";

function ClassSearch() {
  let SearchContext = React.createContext();
  return (
    <>
      <div className={styles.wrapper}>
        <SideBar />
        <UserInfo />
        <SearchResults />
      </div>
    </>
  );
}

export default ClassSearch;
