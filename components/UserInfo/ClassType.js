import Select from "react-select";
import styles from "/styles/ClassSearch.module.css";
import GEN_ED_CLASSES from "./genEdList";

function ClassType(props) {
  return (
    <fieldset className={styles.classType}>
      <span>Give me a : </span>
      <div className={styles.select}>
        <Select options={GEN_ED_CLASSES} onChange={props.onChangeHandler} />
      </div>
    </fieldset>
  );
}

export default ClassType;
