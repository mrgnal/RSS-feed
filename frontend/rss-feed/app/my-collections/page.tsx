'use client'
import React, { useEffect, useState } from 'react'
import RssFeedsMenu from '../components/RssFeed/RssFeeds/RssFeedsMenu'
import RssFeedsHeader from '../components/RssFeed/RssFeeds/RssFeedsHeader'
import style from './page.module.css'
import Image from 'next/image'
import Collection from '../components/RssFeed/Collections/Collection'
import RssFeedMenuMobile from '../components/RssFeed/RssFeeds/RssFeedMenuMobile'

function getWindowSize() {
  const {innerWidth, innerHeight} = window;
  return {innerWidth, innerHeight};
}

const Collections = () => {
  const [isMenuVisible, setIsMenuVisible] = useState<boolean>(false);

  const [windowSize, setWindowSize] = useState(getWindowSize());

  useEffect(() => {
    function handleWindowResize() {
      setWindowSize(getWindowSize());
    }

    window.addEventListener('resize', handleWindowResize);

    return () => {
      window.removeEventListener('resize', handleWindowResize);
    };
  }, []);

  return (
    <>
      <main className={style.main}>
        <RssFeedsMenu isMenuVisible={isMenuVisible} menuVisibleToggle={() => {
              setIsMenuVisible(!isMenuVisible);
          }}/>
        <div className={style.content}>
          <RssFeedsHeader>
            <h2 className={style.title}>Collections</h2>
          </RssFeedsHeader>
          <div className={style.filterContainer}>
            <div className={style.filterContainerLeft}>
              <div className={style.searchContainer}>
                <Image src="/Search.svg" alt='Search' width={20} height={20}/>
                <input placeholder='Filter Collections...' className={style.searchInput}/>
              </div>
            </div>
          </div>
          <div className={style.contentContainer}>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
            <Collection title='Test collection'/>
          </div>
        </div>
        {
          windowSize.innerWidth < 740 &&
          <RssFeedMenuMobile menuVisibleToggle={() => {
            setIsMenuVisible(!isMenuVisible);
          }}/>
        }
      </main>
    </>
  )
}

export default Collections