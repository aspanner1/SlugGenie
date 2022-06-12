import Link from "next/link";
import styles from "/styles/ClassSearch.module.css";
import * as FaIcons from "react-icons/fa";
import { SideBarData } from "/components/SideBar/SideBarData";
import { useState } from "react";

function SideBar() {
  const [sideBar, setSideBar] = useState(false);

  const showSideBar = () => setSideBar(!sideBar);

  return (
    <div className={styles.sidebar}>
      <ul>
        {SideBarData.map((item, index) => {
          return (
            <Link href={item.path} key={index}>
              <li className={styles.menu_item}>
                {item.icon}
                <span className={styles.menu_text}>{item.title}</span>
              </li>
            </Link>
          );
        })}
      </ul>
    </div>
  );
}

export default SideBar;
