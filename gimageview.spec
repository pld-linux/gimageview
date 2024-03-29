#
# Conditional build:
%bcond_with	gtk1	# use GTK+ 1.2.x instead of 2.x.x
#
Summary:	Graphic Viewer
Summary(pl.UTF-8):	Przeglądarka plików graficznych
Name:		gimageview
Version:	0.2.27
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gtkmmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	878a272bae2d79c899a597f9d1dd8078
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gtk.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.homa.ne.jp/~ashie/gimageview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	popt-devel
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	zlib-devel
%if %{with gtk1}
BuildRequires:	glib-devel >= 1.2.6
BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	librsvg-devel >= 1.0.0
BuildRequires:	libxml-devel
Requires:	gdk-pixbuf >= 0.8.0
Requires:	glib >= 1.2.6
Requires:	gtk+ >= 1.2.6
%else
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	pkgconfig
%endif
Requires:	libwmf >= 2:0.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GImageView is a GTK+ based image viewer. It support tabbed browsing,
thumbnail table views, directory tree views, drag and drop, reading
thumbnail cache of other famous image viewers, and flexible user
interface.

%description -l pl.UTF-8
GImageView to oparta na GTK+ przeglądarka obrazków. Pozwala na
przeglądanie z zakładkami, przeglądanie miniaturek i drzew katalogów,
obsługuje drag-n-drop, potrafi odczytywać miniaturki z cache innych
przeglądarek obrazków i ma elastyczny interfejs użytkownika.

%prep
%setup -q
%patch0 -p1 
#%patch1 -p1
%patch2 -p1

rm -f m4/{gettext.m4,libtool.m4}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gtk1:--with-gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gimageview/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%doc %lang(ja) doc/ja/{ChangeLog,NEWS,README,TODO}.ja
%attr(755,root,root) %{_bindir}/gimv
%dir %{_datadir}/gimageview
%dir %{_datadir}/gimageview/pixmaps
%dir %{_datadir}/gimageview/pixmaps/default
%{_datadir}/gimageview/pixmaps/default/*.xpm
%dir %{_libdir}/gimageview
%dir %{_libdir}/gimageview/*
%attr(755,root,root) %{_libdir}/gimageview/*/*.so
%{_desktopdir}/gimageview.desktop
%{_pixmapsdir}/gimv.png
