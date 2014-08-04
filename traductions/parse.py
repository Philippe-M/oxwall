#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ Philippe MALADJIAN (http://www.blogoflip.fr)
# __version__ 1.0

from lxml import etree
from optparse import OptionParser
import os
    
def CreateTranslate():
    srcLanguage = raw_input("path and filename to source file (ex:en/language_en/mobile.xml) : ")
    srcTree = etree.parse(srcLanguage)
    srcRoot = srcTree.getroot()
    for node in srcRoot.xpath("//prefix"):
        srcName = node.get("name")
        srcLabel = node.get("label")
        srcLanguage_tag = node.get("language_tag")
        srcLanguage_label = node.get("language_label")
        
        print "-------------------------------------------"
        print " Source File"
        print srcName + " - " + srcLabel + " - " + srcLanguage_tag + " - " + srcLanguage_label
        print "-------------------------------------------\n"

    outLanguage = raw_input("path and filename to compare file (ex: fr/language_fr/mobile.xml: ")
    outTree = etree.parse(outLanguage)
    outRoot = outTree.getroot()
    for node in outRoot.xpath("//prefix"):
        outName = node.get("name")
        outLabel = node.get("label")
        outLanguage_tag = node.get("language_tag")
        outLanguage_label = node.get("language_label")
        print "-------------------------------------------"
        print " compare File"
        print outName + " - " + outLabel + " - " + outLanguage_tag + " - " + outLanguage_label
        print "-------------------------------------------\n"
        
    root = etree.Element("prefix")
    root.set("name", outName)
    root.set("label", outLabel)
    root.set("language_tag", outLanguage_tag)
    root.set("language_label", outLanguage_label)
    
    for node in srcTree.xpath("//prefix/key"):
        srcKeyName = node.get("name")
        key = etree.SubElement(root, "key")
        key.set("name", srcKeyName)
        try:
            result = outRoot.find(".//*[@name='" + srcKeyName + "']/value").text
            value = etree.SubElement(key, "value")
            value.text = result
        except AttributeError, e:
            result = srcRoot.find(".//*[@name='" + srcKeyName + "']/value").text
            value = etree.SubElement(key, "value")
            value.text = result
            
    outFileName = raw_input("Path and filename to write xml file (ex: out/mobile.xml): ")
    outFile = open(outFileName, "w")
    outFile.write(etree.tostring(root, encoding='utf-8', xml_declaration=True, pretty_print=False))
    outFile.close()

def main():
    try:
        CreateTranslate()

    except KeyboardInterrupt:
        print "\n"
        os._exit(0)

if __name__ == '__main__':
    main()
