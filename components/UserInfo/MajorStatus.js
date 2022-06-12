import styles from "/styles/ClassSearch.module.css";
import React, { useContext } from "react";
import { MAJORS } from "./MajorList";
import Select from "react-select";

function MajorStatus(props) {
  return (
    <>
      <fieldset className={styles.majorDeclaration}>
        <span>I am currently :</span>
        <div className={styles.select}>
          <Select
            id="declared"
            options={[
              {
                label: "Choose one",
                value: "Choose one",
                isDisabled: true,
              },
              { label: "Undeclared", value: "Undeclared" },
              { label: "Declared", value: "Declared" },
            ]}
            onChange={props.onChangeDeclaredHandler}
            ref={props.declaredRef}
          />
        </div>
      </fieldset>
      <fieldset className={styles.majorName}>
        <span>My major is : </span>
        <div className={styles.select}>
          <Select
            aria-invalid="grammar"
            aria-label="Place to select majors"
            closeMenuOnSelect={true}
            options={MAJORS}
            placeholder="Enter your major"
            onChange={props.onChangeMajorHandler}
            ref={props.majorRef}
            id="major"
          />
        </div>
      </fieldset>
    </>
  );
}

export default MajorStatus;
