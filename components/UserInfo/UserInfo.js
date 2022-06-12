import React, { useState, useReducer, useEffect, useRef } from "react";
import MajorStatus from "./MajorStatus";
import ClassType from "./ClassType";
import styles from "/styles/ClassSearch.module.css";

function UserInfo() {
  const STARTING_USER_INFO = {
    declared: false,
    major: "",
    selectMajor: true,
    genEdCategory: "",
    selectGenEd: false,
  };

  const [currentMajor, setCurrentMajor] = useState(undefined);
  const [currentlyDeclared, setCurrentlyDeclared] = useState(undefined);

  useEffect(() => {
    if (currentlyDeclared) {
      localStorage.setItem("declared", currentlyDeclared);
    }

    if (currentMajor) {
      localStorage.setItem("major", currentMajor);
    }
  }, [currentMajor, currentlyDeclared]);

  useEffect(() => {
    let storedDeclarationStatus = localStorage.getItem("declared");
    let storedMajor = localStorage.getItem("major");
    declaredRef.current.setValue({
      label: storedDeclarationStatus,
      value: storedDeclarationStatus,
    });
    majorRef.current.setValue({
      label: storedMajor,
      value: storedMajor,
    });
  }, []);

  let declaredRef = useRef();
  let majorRef = useRef();

  function onChangeMajorHandler(userInput) {
    if (userInput.value) {
      setCurrentMajor(userInput.value);
    }
  }

  function onChangeDeclaredHandler(userInput) {
    if (userInput.value) {
      setCurrentlyDeclared(userInput.value);
    }
  }

  function onSubmitHandler(event) {
    event.preventDefault();
  }

  return (
    <form className={styles.userInfo} method="post" onSubmit={onSubmitHandler}>
      <MajorStatus
        onChangeMajorHandler={onChangeMajorHandler}
        onChangeDeclaredHandler={onChangeDeclaredHandler}
        majorRef={majorRef}
        declaredRef={declaredRef}
      />
      <ClassType />
      <button
        type="submit"
        name="submitUserInfo"
        className={styles.submitUserInfoButton}
      >
        Search
      </button>
    </form>
  );
}

export default UserInfo;

/*
  function userInfoReducer(prevState, action) {
    switch (action.command) {
      case "update": {
        const newState = Object.assign(prevState, action.newValue);
        return newState;
      }
      case "getState": {
        let currentState = prevState;
        console.log(currentState);
        return prevState;
      }
    }
  }

   const [userDetails, setUserDetails] = useReducer(
    userInfoReducer,
    STARTING_USER_INFO
  );
  */
