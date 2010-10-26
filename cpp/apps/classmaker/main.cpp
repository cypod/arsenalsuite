/*
 *
 * Copyright 2003, 2004 Blur Studio Inc.
 *
 * This file is part of the Resin software package.
 *
 * Assburner is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * Assburner is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Resin; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 */
 
#include <qapplication.h>
#include <qdir.h>
#include <qfile.h>

#include "blurqt.h"
#include "mainwindow.h"
#include "schema.h"
#include "sourcegen.h"

static void usage()
{
	LOG_5( "--help, -h\tPrints the command line options" );
	LOG_5( "--schema, -s FILE\tLoads the schema from file FILE" );
	LOG_5( "--output, -o DIR\tOutputs C++ code generated by the loaded schema to DIR/autocore" );
	LOG_5( stoneOptionsHelp() );
}

int main( int argc, char * argv[] )
{
	
#ifdef Q_WS_X11
	bool useGUI = getenv( "DISPLAY" ) != 0;
#else
	bool useGUI = true;
#endif // Q_WS_X11
	QApplication a( argc, argv, useGUI );


	Schema * schema = 0;
	QString configFile = "classmaker.ini";
	QString schemaFile, outputDir;
	QString templateDir = "templates";

	for( int i=1; i<argc; i++ )
	{
		QString arg( argv[i] );
		if( arg == "--schema" || arg == "-s"  ){
			if( i+1==argc ) { usage(); return 1; }
			schemaFile = QString( argv[i+1] );
			if( i<argc && QFile::exists( schemaFile ) ){
				schema = Schema::createFromXmlSchema( schemaFile, /*isfilename=*/true, /*ignoreDocs=*/false );
			}else{
				LOG_1( "File not found: " + schemaFile );
				return 1;
			}
			i++;
		}
		else if( arg == "--output" || arg == "-o" ) {
			if( i+1==argc ) { usage(); return 1; }
			if( !schema ) {
				LOG_1( "Must first specify the schema to load with --schema" );
				return 1;
			}
			if( i >= argc || !QDir( argv[i+1] ).exists() ) {
				LOG_1( "Output Directory not found" );
				return 1;
			}
			outputDir = argv[i+1];
			i++;
		}
		else if ( arg == "--help" || arg == "-h" ) {
			usage();
			return 0;
		}
		else if( arg == "--config" ) {
			if( i+1==argc ) { usage(); return 1; }
			configFile = argv[i+1];
			i++;
		}
		else if( arg == "--templates" || arg == "-t" ) {
			if( i+1==argc ) { usage(); return 1; }
			if( i >= argc || !QDir( argv[i+1] ).exists() ) {
				LOG_1( "template directory not found" );
				return 1;
			}
			templateDir = argv[i+1];
			i++;
		}
	}

	initConfig( configFile );

	if( !outputDir.isEmpty() ) {
		writeSource( schema, outputDir, templateDir );
		return 0;
	}

	initStone( argc, argv );

	if( useGUI ) {
		MainWindow * mw = new MainWindow();
		if( !schemaFile.isEmpty() )
			mw->setFileName( schemaFile );
		if( schema )
			mw->setSchema( schema );
		mw->show();
		a.exec();
		shutdown();
		return 0;
	} else {
		qWarning( "Classmaker usage without xserver is limited to the -s -o options" );
	}
	shutdown();
	return 0;
}

